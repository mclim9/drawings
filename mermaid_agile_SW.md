# Agile SW Development

[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVERcbiAgICBzdWJncmFwaCBTRzFbSXNzdWUgTWFuYWdlbWVudF1cbiAgICAgICAgQVtGaW5kIElzc3VlXSAtLT4gQ1tDcmVhdGUgSXNzdWVdXG4gICAgICAgIEJbQWRkIEZlYXR1cmVdIC0tPiBDW0NyZWF0ZSBJc3N1ZV1cbiAgICAgICAgQy0tPiBEW0lzc3Vlc11cbiAgICBlbmRcblxuICAgIHN1YmdyYXBoIFNHMltTQ1JVTSBNZWV0aW5nXVxuICAgICAgICBSZXZpZXdJc3N1ZXMgLS0-IGFhYWFhYVtEaXNjdXNzIElzc3VlXSAtLT4gVm90ZV9zdG9yeV9wdHMgLS0-QXNzaWduX3N0b3J5X3B0cyAtLT4gUmV2aWV3SXNzdWVzXG4gICAgZW5kXG5cbiAgICBzdWJncmFwaCBTRzNbV29ya11cbiAgICAgICAgdGFrZV9pc3N1ZSAtLT4gZWRpdF9jb2RlIC0tPiBhc2Rme3Njb3BlX2NyZWVwfSAtLSBubyAtLT4gY2xvc2VfaXNzdWVcbiAgICBlbmRcblxuICAgIGFzZGYgLS0geWVzIC0tPiBDXG4gICAgRCAtLT4gUmV2aWV3SXNzdWVzIiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZSwiYXV0b1N5bmMiOnRydWUsInVwZGF0ZURpYWdyYW0iOmZhbHNlfQ)](https://mermaid-js.github.io/mermaid-live-editor/edit/##eyJjb2RlIjoiZ3JhcGggVERcbiAgICBzdWJncmFwaCBTRzFbSXNzdWUgTWFuYWdlbWVudF1cbiAgICAgICAgQVtGaW5kIElzc3VlXSAtLT4gQ1tDcmVhdGUgSXNzdWVdXG4gICAgICAgIEJbQWRkIEZlYXR1cmVdIC0tPiBDW0NyZWF0ZSBJc3N1ZV1cbiAgICAgICAgQy0tPiBEW0lzc3Vlc11cbiAgICBlbmRcblxuICAgIHN1YmdyYXBoIFNHMltTQ1JVTSBNZWV0aW5nXVxuICAgICAgICBSZXZpZXdJc3N1ZXMgLS0-IGFhYWFhYURpc2N1c3MgLS0-IFZvdGVfc3RvcnlfcHRzIC0tPkFzc2lnbl9zdG9yeV9wdHMgLS0-IFJldmlld0lzc3Vlc1xuICAgIGVuZFxuXG4gICAgc3ViZ3JhcGggU0czW1dvcmtdXG4gICAgICAgIHRha2VfaXNzdWUgLS0-IGVkaXRfY29kZSAtLT4gYXNkZntzY29wZV9jcmVlcH0gLS0gbm8gLS0-IGNsb3NlX2lzc3VlXG4gICAgZW5kXG5cbiAgICBhc2RmIC0tIHllcyAtLT4gQ1xuICAgIEQgLS0-IFJldmlld0lzc3VlcyIsIm1lcm1haWQiOiJ7XG4gIFwidGhlbWVcIjogXCJkZWZhdWx0XCJcbn0iLCJ1cGRhdGVFZGl0b3IiOmZhbHNlLCJhdXRvU3luYyI6dHJ1ZSwidXBkYXRlRGlhZ3JhbSI6ZmFsc2V9)

```mermaid
graph TD
    subgraph SG1[issueList]
        A[Find Issue] --> C[Create Issue]
        B[Add Feature] --> C[Create Issue]
        C--> D[Issues]
    end

    subgraph SG2[SCRUM Meeting]
        ReviewIssues --> Discuss --> Assign_number --> ReviewIssues
    end

    subgraph SG3[Work]
        take_issue --> edit_code --> scope_creep --> close_ticket
        close_ticket --> take_issue
    end

    scope_creep --> C
    D --> ReviewIssues
```
