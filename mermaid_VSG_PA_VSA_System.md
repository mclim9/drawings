# RF Test System
- VSG --> Coupler --> PA --> Coupler --> VSA
[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggTFJcbiAgICBjbGFzc0RlZiBkZWZhdWx0IGZpbGw6IzBhZSxzdHJva2U6IzAwMCxzdHJva2Utd2lkdGg6MXB4XG4gICAgc3R5bGUgZ2VuIGZpbGw6IzlkNSxzdHJva2U6IzAwMCxzdHJva2Utd2lkdGg6MXB4O1xuICAgIHN0eWxlIGFuYSBmaWxsOiM5ZDUsc3Ryb2tlOiMwMDAsc3Ryb2tlLXdpZHRoOjFweDtcblxuICAgIHN1YmdyYXBoIGdlbltHZW5lcmF0aW9uXVxuICAgICAgICBWU0cxIC0tPiBjaXJjdWxhdG9yLTFcbiAgICAgICAgY2lyY3VsYXRvci0xIC0tPiBjb21iaW5lclxuICAgICAgICBWU0cyIC0tPiBjaXJjdWxhdG9yLTJcbiAgICAgICAgY2lyY3VsYXRvci0yIC0tPiBjb21iaW5lclxuICAgICAgICBjb21iaW5lciAtLT4gY291cGxlci1zXG4gICAgICAgIFBNLVMgLS0-IGNvdXBsZXItc1xuICAgIGVuZFxuXG4gICAgICAgIGNvdXBsZXItcyAtLT4gUEFcbiAgICAgICAgUEEgLS0-IGNvdXBsZXItbVxuXG4gICAgc3ViZ3JhcGggYW5hW0FuYWx5c2lzXVxuICAgICAgICBjb3VwbGVyLW0gLS0-IFZTQVxuICAgICAgICBjb3VwbGVyLW0gLS0-IFBNLU1cbiAgICBlbmQiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlLCJhdXRvU3luYyI6dHJ1ZSwidXBkYXRlRGlhZ3JhbSI6ZmFsc2V9)](https://mermaid-js.github.io/mermaid-live-editor/edit/##eyJjb2RlIjoiZ3JhcGggTFJcbiAgICBjbGFzc0RlZiBkZWZhdWx0IGZpbGw6IzBhZSxzdHJva2U6IzAwMCxzdHJva2Utd2lkdGg6MXB4XG4gICAgc3R5bGUgZ2VuIGZpbGw6IzlkNSxzdHJva2U6IzAwMCxzdHJva2Utd2lkdGg6MXB4O1xuICAgIHN0eWxlIGFuYSBmaWxsOiM5ZDUsc3Ryb2tlOiMwMDAsc3Ryb2tlLXdpZHRoOjFweDtcblxuICAgIHN1YmdyYXBoIGdlbltHZW5lcmF0aW9uXVxuICAgICAgICBWU0cxIC0tPiBjaXJjdWxhdG9yLTFcbiAgICAgICAgY2lyY3VsYXRvci0xIC0tPiBjb21iaW5lclxuICAgICAgICBWU0cyIC0tPiBjaXJjdWxhdG9yLTJcbiAgICAgICAgY2lyY3VsYXRvci0yIC0tPiBjb21iaW5lclxuICAgICAgICBjb21iaW5lciAtLT4gY291cGxlci1zXG4gICAgICAgIFBNLVMgLS0-IGNvdXBsZXItc1xuICAgIGVuZFxuXG4gICAgICAgIGNvdXBsZXItcyAtLT4gUEFcbiAgICAgICAgUEEgLS0-IGNvdXBsZXItbVxuXG4gICAgc3ViZ3JhcGggYW5hW0FuYWx5c2lzXVxuICAgICAgICBjb3VwbGVyLW0gLS0-IFZTQVxuICAgICAgICBjb3VwbGVyLW0gLS0-IFBNLU1cbiAgICBlbmQiLCJtZXJtYWlkIjoie1xuICBcInRoZW1lXCI6IFwiZGVmYXVsdFwiXG59IiwidXBkYXRlRWRpdG9yIjp0cnVlLCJhdXRvU3luYyI6dHJ1ZSwidXBkYXRlRGlhZ3JhbSI6dHJ1ZX0)

```mermaid
graph LR
    classDef default fill:#0ae,stroke:#000,stroke-width:1px
    style gen fill:#9d5,stroke:#000,stroke-width:1px;
    style ana fill:#9d5,stroke:#000,stroke-width:1px;

    subgraph gen[Generation]
        VSG1 --> circulator-1
        circulator-1 --> combiner
        VSG2 --> circulator-2
        circulator-2 --> combiner
        combiner --> coupler-s
        PM-S --> coupler-s
    end

        coupler-s --> PA
        PA --> coupler-m

    subgraph ana[Analysis]
        coupler-m --> VSA
        coupler-m --> PM-M
    end
```
