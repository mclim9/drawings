%% https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggTFJcbiAgICBDb250ZXN0QmFzZTE3XzMyIC0tPiBOSS1Nb3Rpb24gXG4gICAgQ29udGVzdEJhc2UxOF82NCAtLSBEZWMgLS0-IDY0X3RvXzMyX01pZGRsZXdhcmVcbiAgICA2NF90b18zMl9NaWRkbGV3YXJlIC0tPiBOSS1Nb3Rpb25cbiAgICBOSS1Nb3Rpb24gLS0-IEZsZXhDb250cm9sMzIuZGxsIFxuICAgIEZsZXhDb250cm9sMzIuZGxsIC0tPiBIb3dsYW5kX0NvbnRyb2xsZXJcbiAgICAiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ

graph LR
    ContestBase17_32 --> NI-Motion 
    ContestBase18_64 -- Dec --> 64_to_32_Middleware
    64_to_32_Middleware --> NI-Motion
    NI-Motion --> FlexControl32.dll 
    FlexControl32.dll --> Howland_Controller
    