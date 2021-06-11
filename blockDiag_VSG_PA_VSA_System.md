# Blockdiag Drawing

[blockDiag-api](https://www.blockdiag-api.com/ui)
[blockDiag](http://interactive.blockdiag.com/)

```blockdiag
blockdiag {
    // Global
    default_fontsize = 20;
    
    // Block Definition
    DUT [color = "#888888", textcolor="#FFFFFF"];
    VSA [icon = "https://cdn.rohde-schwarz.com/pws/product/f_1/fsw/FSW-Signal-Spectrum-Analyzer_2018_list_product_list.jpg"]
    VSG1 [icon = "https://cdn.rohde-schwarz.com/pws/product/s_1/smw200a/SMW200A_front_stage_landscape.jpg"]
    VSG2 [icon = "https://cdn.rohde-schwarz.com/pws/product/s_1/smw200a/SMW200A_front_stage_landscape.jpg"]
    PM-S [icon = 'https://cdn.rohde-schwarz.com/pws/product/n_1/nrpxxs_sn/NRP18S_front_stage_landscape.jpg']
    PM-M [icon = 'https://cdn.rohde-schwarz.com/pws/product/n_1/nrpxxs_sn/NRP18S_front_stage_landscape.jpg']
    
    // Groups
    group{
        color='#009fff';
        shape = 'line';
        label = 'Source';
        VSG1; VSG2; Combiner; CouplerS; PM-S}
    group{
        color='#009fff';
        shape = 'line';
        label = 'Measure';
        CouplerM; VSA; PM-M}
    
    // Routes
    VSG1 -> Combiner;
    VSG2 -> Combiner;
    Combiner -> CouplerS
    CouplerS -> PM-S[label = "monitor", folded];
    CouplerS -> DUT;
    DUT -> CouplerM;
    CouplerM -> PM-M[label = "monitor", folded];
    CouplerM -> VSA;
}
```
