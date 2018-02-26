# Supergroups
<p align="center">
  
  <h3 align="center">Scripts for Homologous Supergroups's inference</h3>

  <p align="center">
    New approach for the identification of homologous genes, based on the reconciliation of the results of two different methodologies
    <br>
    <br>
    <br>
    (The scripts use as input the format of the OrthoMCL and OMA results, but can be adapted to any other tool)
    <br>
    <br>
    <img src="https://github.com/HomologousSupergroups/Supergroups/blob/master/Figura%201.new.jpg">
    <br>
    <br>
    <br>
  Flowchart of the study: Description of the steps and materials used in this study for the inference of homologous Supergroups. 
  </p>
</p>

<br>

## Table of contents

- [Preparation of the homolog database](#Preparation-of-the-homolog-database)
- [Detection of Conserved Domains (CDD) with RpsBLAST](#Detection-of-Conserved-Domains-(CDD)-with-RpsBLAST)
- [Identification of Protein Families (Pfam-A) with CLADE ](#Identification-of-Protein-Families-(Pfam-A)-with-CLADE)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [Community](#community)
- [Versioning](#versioning)
- [Creators](#creators)
- [Copyright and license](#copyright-and-license)

## Preparation of the homolog database


The preparation of the homologous database is done using 2 different approaches for detection of homology in complete genomes: OMA and OrthoMCL

- [Download the complete genomes.](ftp.ncbi.nlm.nih.gov/genomes/refseq/)
- [Download and execute OrthoMCL.](http://orthomcl.org/common/downloads/software/)
   <br> Execute OrthoMCL with 1E-05 as E-value cutoff
- [Download and execute OMA.](http://omabrowser.org/standalone/)
   <br> Execute OMA with default parameters

The output of the 2 software is the homolog database itself.


## Detection of Conserved Domains (CDD) with RPS-BLAST 

- [Download RPS-BLAST.](https://www.ncbi.nlm.nih.gov/) 
- [Download last version of CDD](https://www.ncbi.nlm.nih.gov/Structure/cdd/cdd.shtml). 
    <br> Execute RPS-BLAST with 1E-05 as E-value cutoff
    
## Identification of Protein Families (Pfam-A) with CLADE 

- [Download CLADE](http://www.lcqb.upmc.fr/CLADE). 
  <br> Execute CLADE with 1E-05 as E-value cutoff
    

```
Example for CDD:
XP_009310444.1	99707
XP_004261170.1	99716
XP_004185777.1	99738
XP_004258620.1	99738
XP_004259653.1	99738
XP_002140281.1	99747
XP_009307740.1	99751

Example for Pfam:

XP_009310819.1	PF00004
XP_002141599.1	PF00004
XP_009313373.1	PF00004
XP_004255528.1	PF00004
XP_009306220.1	PF00004
XP_002139818.1	PF00004
XP_002140754.1	PF00004

```

## Reconciliation algorithm – inference of Supergroups
## Division of the homologous groups inferred by OrthoMCL and OMA into 3 categories 


Have a bug or a feature request? Please first read the [issue guidelines](https://github.com/twbs/bootstrap/blob/master/CONTRIBUTING.md#using-the-issue-tracker) and search for existing and closed issues. If your problem or idea is not addressed yet, [please open a new issue](https://github.com/twbs/bootstrap/issues/new).


## Documentation

Bootstrap's documentation, included in this repo in the root directory, is built with [Jekyll](https://jekyllrb.com/) and publicly hosted on GitHub Pages at <https://getbootstrap.com/>. The docs may also be run locally.

Documentation search is powered by [Algolia's DocSearch](https://community.algolia.com/docsearch/). Working on our search? Be sure to set `debug: true` in the `_scripts.html` include.

### Running documentation locally

1. Run through the [tooling setup](https://getbootstrap.com/docs/4.0/getting-started/build-tools/#tooling-setup) to install Jekyll (the site builder) and other Ruby dependencies with `bundle install`.
2. Run `npm install` to install Node.js dependencies.
3. Run `npm run test` (or a specific NPM script) to rebuild distributed CSS and JavaScript files, as well as our docs assets.
4. From the root `/bootstrap` directory, run `npm run docs-serve` in the command line.
5. Open `http://localhost:9001` in your browser, and voilà.

Learn more about using Jekyll by reading its [documentation](https://jekyllrb.com/docs/home/).

### Documentation for previous releases

- For v2.3.2: <https://getbootstrap.com/2.3.2/>
- For v3.3.x: <https://getbootstrap.com/docs/3.3/>

[Previous releases](https://github.com/twbs/bootstrap/releases) and their documentation are also available for download.


## Contributing

Please read through our [contributing guidelines](https://github.com/twbs/bootstrap/blob/master/CONTRIBUTING.md). Included are directions for opening issues, coding standards, and notes on development.

Moreover, if your pull request contains JavaScript patches or features, you must include [relevant unit tests](https://github.com/twbs/bootstrap/tree/master/js/tests). All HTML and CSS should conform to the [Code Guide](https://github.com/mdo/code-guide), maintained by [Mark Otto](https://github.com/mdo).

Editor preferences are available in the [editor config](https://github.com/twbs/bootstrap/blob/master/.editorconfig) for easy use in common text editors. Read more and download plugins at <http://editorconfig.org/>.


## Community

Get updates on Bootstrap's development and chat with the project maintainers and community members.

- Follow [@getbootstrap on Twitter](https://twitter.com/getbootstrap).
- Read and subscribe to [The Official Bootstrap Blog](https://blog.getbootstrap.com/).
- Join [the official Slack room](https://bootstrap-slack.herokuapp.com/).
- Chat with fellow Bootstrappers in IRC. On the `irc.freenode.net` server, in the `##bootstrap` channel.
- Implementation help may be found at Stack Overflow (tagged [`bootstrap-4`](https://stackoverflow.com/questions/tagged/bootstrap-4)).
- Developers should use the keyword `bootstrap` on packages which modify or add to the functionality of Bootstrap when distributing through [npm](https://www.npmjs.com/browse/keyword/bootstrap) or similar delivery mechanisms for maximum discoverability.


## Versioning

For transparency into our release cycle and in striving to maintain backward compatibility, Bootstrap is maintained under [the Semantic Versioning guidelines](http://semver.org/). Sometimes we screw up, but we'll adhere to those rules whenever possible.

See [the Releases section of our GitHub project](https://github.com/twbs/bootstrap/releases) for changelogs for each release version of Bootstrap. Release announcement posts on [the official Bootstrap blog](https://blog.getbootstrap.com/) contain summaries of the most noteworthy changes made in each release.


## Creators

**Mark Otto**

- <https://twitter.com/mdo>
- <https://github.com/mdo>

**Jacob Thornton**

- <https://twitter.com/fat>
- <https://github.com/fat>


## Copyright and license

Code and documentation copyright 2011-2018 the [Bootstrap Authors](https://github.com/twbs/bootstrap/graphs/contributors) and [Twitter, Inc.](https://twitter.com) Code released under the [MIT License](https://github.com/twbs/bootstrap/blob/master/LICENSE). Docs released under [Creative Commons](https://github.com/twbs/bootstrap/blob/master/docs/LICENSE).
