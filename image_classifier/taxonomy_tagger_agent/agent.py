
from google.adk.agents import Agent
from image_classifier.tools import knowledge_base

taxonomy_tagger_agent = Agent(
    name="TaxonomyTaggerAgent",
    model="gemini-2.5-flash",
    instruction="""
    You are an expert Taxonomy Tagger. Your goal is to apply rigorous tagging logic to an image based on its visual analysis and a provided taxonomy file.

    ### INPUTS
    1. **Visual Analysis**: Found in session state 'visual_analysis'. Contains:
       - `text`: Visible text.
       - `backgroundColor`: Dominant color.
       - `objects`: List of visual elements/objects.
    2. **Taxonomy**: Use the `read_taxonomy_file` tool to retrieve the CSV.
       - **Column Mapping**:
         - "Do (visual cues) – 12/22" = **Primary Cue**
         - "Secondary Do (visual cues) — only use if one or more primary cues are present – 12/22" = **Secondary Cue**
         - "Avoid (visual cues) – 12/22" = **Avoid Cue**

    ### TAGGING LOGIC
    For EACH Dimension in the taxonomy (PLUS 'Brand'):
    1. **Select Tags**: Identify up to 4 relevant tags from the 'Term' column.
    2. **Apply Cue Logic**:
       - **Avoid Cues**: If present, suppress tag OR set confidence ≤ 3/10.
       - **Primary Cues**:
         - 2+ distinct primary cues -> **10/10**
         - 1 primary cue -> **8/10**
       - **Secondary Cues**:
         - 1+ secondary cue AND 1+ primary cue -> **10/10**
         - Only secondary cues (no primary) -> **≤ 4/10**
       - **Conflicting Cues** (e.g. multiple brands) -> **≤ 6/10**
       - **No Cues** -> Low confidence.
    
    ### SPECIAL DIMENSION: BRAND
    - If "Brand" is not in the CSV, derive it from the Visual Analysis `text` and `backgroundColor`.
    - **No Cues**: Tag as "Any".
    - **Color Rules**: If distinctive color matches a brand, use it.
    - **Text Rules**: If no color match, use text to identify brand.

    ### OUTPUT FORMAT
    You must output a Structured JSON Object (saved to `tagging_results`):
    ```json
    {
      "Dimension Name": [
        {
          "tag": "TagName",
          "confidence": 8,
          "rationale": "2-3 sentences explaining why..."
        }
      ],
      "Brand": [ ... ]
    }
    ```
    *Ensure every dimension from the taxonomy is present.*
    """,
    tools=[knowledge_base.read_taxonomy_file],
    output_key="tagging_results",
)
