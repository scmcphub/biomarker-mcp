from pydantic import (
    Field,
    ValidationInfo,
    computed_field,
    field_validator,
    model_validator,BaseModel
)
from typing import Optional, List, Dict, Union, Literal, Tuple


Genetype_items = Literal["protein-coding", "lncRNA", "IG_C_gene", "transcribed_unprocessed_pseudogene", "TR_C_gene", "processed_pseudogene", "transcribed_processed_pseudogene", "IG_V_gene", "transcribed_unitary_pseudogene", "TR_V_gene", "polymorphic_pseudogene", "unprocessed_pseudogene", "snoRNA", "miRNA", "IG_C_pseudogene", "TEC", "snRNA", "misc_RNA", "scaRNA", "IG_V_pseudogene", "ribozyme", "translated_unprocessed_pseudogene", "scRNA", "IG_J_gene"]

Tissue_class_items = Literal['Brain','Kidney','Blood','Lung','Gonad','Undefined','Intestine','Bone marrow','Liver','Embryo','Trachea','Skin','Adipose tissue','Spleen','Pancreas','Breast','Eye','Stomach','Heart','Esophagus','Blood vessel','Ovary','Bone','Muscle','Thymus','Lymph node','Prostate','Testis','Articular Cartilage','Bladder','Uterus','Nose','Pharynx','Bile duct','Tooth','Lymphoid tissue','Placenta','Lymph','Suprarenal gland','Epithelium','Gastrointestinal tract','Aorta','Artery','Salivary gland','Nerve','Germ','Soft tissue','Spinal cord','Airway','Tonsil','Ear','Colon','Mammary gland','Endometrium','Oral cavity','Thyroid','Cartilage','Peritoneal fluid','Decidua','Sputum','Tendon','Skeletal muscle','Umbilical cord','Urine','Nasopharynx','Intervertebral disc','Synovium','Tongue','Uterine cervix','Hindlimb','Genitals','Thorax','Cerebral organoid','Vein','Fetal brain','Periodontium','Belly','Gall bladder','Cerebellum','Peritoneum','Abdomen','Renal Tubule','Limb','Ligament','Vagina','Neck','Oviduct','Biliary tract','Epidermis','Meniscus','Fetal striatum','Nasal','limb','Synovial','Cornea','Fetus','Scalp','Nodose','Articulation','Head and neck','Joint','Larynx','Gut','Periosteum','Foot','Pylorus','Palatine tonsil','Peyer patch','Macrovessel','Hind limb','Cavernosum','Embryos','Adventitia','Knee joint','Dorsal root ganglia','Synovial fluid','Amniotic fluid','Omentum','Lumbar','PeriBiliary cell gland','Airway epithelium','Inferior colliculus','Intestine/Proliferating ECs pool','Non-Vasculature','Respiratory tract','lymph node','Fundic gland','Bronchus','Adrenal gland','Pleura','Head and Neck','Mammary Gland','Neural tube','Mouth','Endocrine organ','Flesh','Fetal liver','Esophageal','Head','Endocardium','Diaphragm','Cervix','Taste bud','Skeletal Muscle','Sinus tissue']

cellmarker_columns = Literal['species', 'tissue_class', 'tissue_type', 'uberonongology_id',
       'cancer_type', 'cell_type', 'cell_name', 'cellontology_id', 'marker',
       'Symbol', 'GeneID', 'Genetype', 'Genename', 'UNIPROTID',
       'technology_seq', 'marker_source', 'PMID', 'Title', 'journal', 'year']

['species', 'tissue_class', 'tissue_type', 'cancer_type', 'cell_type', 'cell_name','Symbol', 'GeneID', 'Genetype']

class CellMarkerDB(BaseModel):
    species: List[Literal["Human", "Mouse"]] = Field(default=["Human", "Mouse"], description="The species for the query (Human or Mouse)")
    tissue_class: List[Tissue_class_items] = Field(default=None, description="The tissue class for the query")
    tissue_type: List[str] = Field(default=None, description="The tissue type for the query")
    cancer_type: List[str] = Field(default=None, description="The cancer type for the query")
    cell_type: List[Literal["Normal cell", "Cancer cell"]] = Field(default=None, description="Normal cell or Cancer cell for the query ")
    cell_name: List[str] = Field(default=None, description="The cell name for the query")
    Symbol: List[str] = Field(default=None, description="The Symbol for the query")
    Genetype: List[Genetype_items] = Field(default=None, description="The Gene type for the query")
    GeneID: List[str] = Field(default=None, description="The Gene ID for the query")
    show_num: int = Field(default=10, description="The number of records to show")
    show_columns: List[cellmarker_columns] = Field(
        default=['species', 'tissue_class', 'tissue_type', 'cancer_type', 'cell_type', 'cell_name','Symbol', 'GeneID', 'Genetype'],
         description="The columns to show")
    # cellontology_id: str = Field(default="CL:0000066", description="The Cell Ontology ID for the query")
    # marker: str = Field(default="CD44", description="The marker for the query")
    # GeneID: str = Field(default="960", description="The Gene ID for the query")
    # Genetype: str = Field(default="protein-coding", description="The Gene type for the query")
    # Genename: str = Field(default="CD44 molecule", description="The Gene name for the query")
    # UNIPROTID: str = Field(default="P16070", description="The UNIPROT ID for the query")
    # technology_seq: str = Field(default="RNA-seq", description="The technology sequence for the query")
    # marker_source: str = Field(default="CellMarker", description="The marker source for the query")
    # PMID: str = Field(default="12345678", description="The PMID for the query")
    # Title: str = Field(default="Example Research Paper", description="The Title for the query")
    # journal: str = Field(default="Nature", description="The journal for the query")
    # year: int = Field(default=2023, description="The year for the query")
    # uberonongology_id: str = Field(default="UBERON:0000310", description="The UBERON ontology ID for the query")

