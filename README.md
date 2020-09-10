> Introduction (please delete after reading):  
[standard-GEM](https://github.com/MetabolicAtlas/standard-GEM) is a template repository that aims to standardize the format of genome-scale metabolic models (GEMs) versioned with git. In addition to encouraging the open-sourcing of GEMs, it facilitates the import of GEMs into databases and online websites. Moreover, it provides the community with a familiar structure that is easy to adopt through this repository itself. The template comes with a set of requirements and recommendations, packaged as to-do items in a hidden Markdown file in this repository `.standard-GEM.md`. After downloading this repository, or using it as a template, those to-do items provide guidance to how adherence to the standard can be obtained.

> Instructions for this `README` (please delete after reading):  
This is the `README.md` template provided by [standard-GEM](https://github.com/MetabolicAtlas/standard-GEM) and was crafted to cover most use-cases.  
Feel free to edit this template `README`. Blanks are indicated by `{{ test }}`. One may use a search function to find these `{{`. Here are some examples of blanks used throughout this file: `{{organization or username}}` is the organization name or username for this GitHub repository, eg. `SysBioChalmers`; `{{repository name}}` is the name of this GitHub repository, eg. `yeast-GEM`.  
If you find this template does not fit your needs, we would appreciate if you could report this by creating a new issue on [standard-GEM](https://github.com/MetabolicAtlas/standard-GEM/issues).


## {{repository name}}: {{repository description}}

[![Version](https://badge.fury.io/gh/{{organization or username}}%2F{{repository name}}.svg)](https://badge.fury.io/gh/sysbiochalmers/yeast-gem)  
[![Zenodo](https://zenodo.org/badge/{{Zenodo ID}}.svg)](https://zenodo.org/badge/latestdoi/{{Zenodo ID}})  
[![Gitter chat](https://badges.gitter.im/{{organization or username}}/{{repository name}}.svg)](https://gitter.im/{{organization or username}}/{{repository name}})


#### Description

{{ fill in a short description or the paper abstract }}


#### Citation

{{ provide the citation once available, for example:
  > Lu, H., Li, F., Sánchez, B.J. et al (2019). A consensus S. cerevisiae metabolic model Yeast8 and its ecosystem for comprehensively probing cellular metabolism. Nat Commun 10, 3586 [doi:10.1038/s41467-019-11581-3](https://doi.org/10.1038/s41467-019-11581-3)

}}


#### Keywords

> Keywords are be separated by semicolons.
> The `Model source` field contains the source(s) of the current model, eg existing GEMs. If possible, use the Markdown format to add the URL with the DOI. The (NCBI) taxonomy ID should be provided in the [format from identifiers.org](https://registry.identifiers.org/registry/taxonomy). For the genome identifier, please provide the ENA/GenBank/RefSeq identifier via *identifiers.org*, or from other sources such as PATRIC or KBase.  

**Utilisation:** {{ experimental data reconstruction; multi-omics integrative analysis;, _in silico_ strain design; model template }}  
**Field:** {{ metabolic-network reconstruction }}  
**Type of model:** {{ reconstruction; curated }}  
**Model source:** {{ [YeastMetabolicNetwork](http://doi.org/10.1038/nbt1492) }}  
**Omic source:** {{ genomics; metabolomics }}  
**Taxonomic name:** {{ _Saccharomyces cerevisiae_ }}  
**Taxonomy ID:** {{ [taxonomy:559292](https://identifiers.org/taxonomy:559292) }}  
**Genome ID:** {{ [insdc.gca:GCA_000146045.2](https://identifiers.org/insdc.gca:GCA_000146045.2)  }}  
**Metabolic system:** {{ general metabolism }}  
**Tissue:**  
**Bioreactor:**    
**Cell type:**  
**Cell line:**  
**Strain:** {{ S288C }}  
**Condition:** {{ aerobic; glucose-limited; defined media }}  


### Installation

{{ Be mindful of users who do not have a typical background - provide a clear overview of the required software. Also, there might be different requirements for users and collaborators. }}


### Usage

{{ Describe how to load and save the model. }}


### Contributing

Contributions are always welcome! Please read the [contributing guideline](.github/CONTRIBUTING.md) to get started.


### Contributors

Code contributors are reported automatically by GitHub under [Contributors](https://github.com/{{organization or username}}/{{repository name}}/graphs/contributors), while other contributions come in as [Issues](https://github.com/{{organization or username}}/{{repository name}}/issues).