# 0_plane
## Configured CSP
### CSP meta tag and script tag with integrity
```
<meta http-equiv="Content-Security-Policy" content="default-src *; script-src 'self' 'strict-dynamic'; style-src 'self'; connect-src 'self'; base-uri 'none'">
```

### Warnings
```
```

## Time
### System(sec) - 30times
```
0.02
0.02
0.022
0.02
0.021
0.02
0.021
0.02
0.019
0.022
0.015
0.015
0.015
0.016
0.015
0.015
0.016
0.018
0.013
0.013
0.014
0.016
0.017
0.015
0.015
0.015
0.015
0.018
0.015
```

### Browser(sec)
|before|after|
|:-:|:-:|
|||


# 1_javascript_scheme
## Configured CSP
### CSP meta tag and script tag with integrity
```
<meta http-equiv="Content-Security-Policy" content="default-src *; script-src 'self' 'strict-dynamic'; style-src 'self'; connect-src 'self'; base-uri 'none'">
```

### Warnings
```
[-] javascript: scheme in http://localhost:8080/1_javascript_scheme/index.php
```

## Time
### System(sec)
```
0.019
0.02
0.019
0.02
0.017
0.019
0.02
0.016
0.018
0.018
```

### Browser(sec)
|before|after|
|:-:|:-:|
|||


# 2_external_js
## Configured CSP
### CSP meta tag and script tag with integrity
```
<meta http-equiv="Content-Security-Policy" content="default-src *; script-src 'self' http://localhost:8080 'sha256-gZmBnd4RznX/R53Rxj7t8Swp7HDysCKvy25yYD5QGfE=' 'strict-dynamic'; style-src 'self'; connect-src 'self'; base-uri 'none'">

<script integrity="sha256-gZmBnd4RznX/R53Rxj7t8Swp7HDysCKvy25yYD5QGfE=" src="./script.js"></script>
```

### Warnings
```
```

## Time
### System(sec)
```
0.029
0.028
0.026
0.026
0.031
0.024
0.024
0.024
0.028
0.031
0.027
0.028
0.027
0.026
0.024
0.035
0.026
0.028
0.028
0.027
0.026
0.032
0.025
0.033
0.029
0.025
0.026
0.037
0.031
0.031
0.032
```

### Browser(sec)
|before|after|
|:-:|:-:|
|||


# 3_inline_script
## Configured CSP
### CSP meta tag and script tag with integrity
```
<meta http-equiv="Content-Security-Policy" content="default-src *; script-src 'self' 'sha256-uxVHDkI2VVxiLrjNPK9Qlg7amPkHZVarv+HgmvH7IUI=' 'strict-dynamic'; style-src 'self'; connect-src 'self'; base-uri 'none'">
```

### Warnings
```
```

## Time
### System(sec)
```
0.031
0.023
0.021
0.025
0.023
0.021
0.017
0.019
0.019
0.019
```

### Browser(sec)
|before|after|
|:-:|:-:|
|||


# 4_external_style
## Configured CSP
### CSP meta tag and script tag with integrity
```
<meta http-equiv="Content-Security-Policy" content="default-src *; script-src 'self' 'strict-dynamic'; style-src 'self' http://localhost:8080; connect-src 'self'; base-uri 'none'">
```

### Warnings
```
```

## Time
### System(sec)
```
0.019
0.018
0.022
0.021
0.018
0.018
0.024
0.022
0.018
0.018
```

### Browser(sec)
|before|after|
|:-:|:-:|
|||


# 5_inline_style
## Configured CSP
### CSP meta tag and script tag with integrity
```
<meta http-equiv="Content-Security-Policy" content="default-src *; script-src 'self' 'strict-dynamic'; style-src 'self' 'sha256-caL/t84GBpmtv6vzuELR38kq9LWs/L5BujNjEy1csGk='; connect-src 'self'; base-uri 'none'">
```

### Warnings
```
[-] style attribute in http://localhost:8080/5_inline_style/index.php
```

## Time
### System(sec)
```
0.025
0.02
0.018
0.024
0.018
0.017
0.017
0.015
0.022
0.018
```

### Browser(sec)
|before|after|
|:-:|:-:|
|||


# 6_script_with_url
## Configured CSP
### CSP meta tag and script tag with integrity
```
<meta http-equiv="Content-Security-Policy" content="default-src *; script-src 'self' http://localhost:8080 'sha256-b0wIol3V1kTL/TiBO5xkMC3MCsxQSGY/u6kUedKpvh4=' 'sha256-rr+HAv/rvjCyw6HOiKuNCRhCMB7YDTSkVk9fiq2+U2k=' 'sha256-AbpHGcgLb+kRsJGnwFEktk7uzpZOCcBY74+YBdrKVGs=' 'strict-dynamic'; style-src 'self'; connect-src 'self' https://code.jquery.com; base-uri 'none'">

<script integrity="sha256-b0wIol3V1kTL/TiBO5xkMC3MCsxQSGY/u6kUedKpvh4=" src="./xhr_jquery.js"></script>
<script integrity="sha256-rr+HAv/rvjCyw6HOiKuNCRhCMB7YDTSkVk9fiq2+U2k=" src="./xhr_react.js"></script>
```

### Warnings
```
```

## Time
### System(sec)
```
0.037
0.033
0.033
0.033
0.033
0.029
0.033
0.035
0.033
0.033
```

### Browser(sec)
|before|after|
|:-:|:-:|
|||


# 7_inner_outer_html
## Configured CSP
### CSP meta tag and script tag with integrity
```
<meta http-equiv="Content-Security-Policy" content="default-src *; script-src 'self' http://localhost:8080 'sha256-llIEnPoqBHAkMW9ma2Fyh9gMKWEcYXva3SbAAxHpyYs=' 'strict-dynamic'; style-src 'self'; connect-src 'self'; base-uri 'none'">

<script integrity="sha256-llIEnPoqBHAkMW9ma2Fyh9gMKWEcYXva3SbAAxHpyYs=" src="./script.js"></script>
```

### Warnings
```
[-] innerHTML / outerHTML in http://localhost:8080/7_inner_outer_html/script.js (Line 5)
[-] innerHTML / outerHTML in http://localhost:8080/7_inner_outer_html/script.js (Line 6)
```

## Time
### System(sec)
```
0.027
0.027
0.026
0.023
0.028
0.038
0.029
0.024
0.023
0.024
```

### Browser(sec)
|before|after|
|:-:|:-:|
|||


# 8_document_write_writeln
## Configured CSP
### CSP meta tag and script tag with integrity
```
<meta http-equiv="Content-Security-Policy" content="default-src *; script-src 'self' http://localhost:8080 'sha256-1NYcwZPUGTVgwxOoV8wIyICVCMhB3F9b3H22XnvuEVw=' 'strict-dynamic'; style-src 'self'; connect-src 'self'; base-uri 'none'">

<script integrity="sha256-1NYcwZPUGTVgwxOoV8wIyICVCMhB3F9b3H22XnvuEVw=" src="./script.js"></script>
```

### Warnings
```
[-] document.write(ln) in http://localhost:8080/8_document_write_writeln/script.js (Line 1)
[-] document.write(ln) in http://localhost:8080/8_document_write_writeln/script.js (Line 2)
```

## Time
### System(sec)
```
0.025
0.025
0.03
0.024
0.026
0.024
0.024
0.025
0.026
0.029
```

### Browser(sec)
|before|after|
|:-:|:-:|
|||


# 9_eval
## Configured CSP
### CSP meta tag and script tag with integrity
```
<meta http-equiv="Content-Security-Policy" content="default-src *; script-src 'self' http://localhost:8080 'sha256-1MV04PDgio8yygougSv5TFU7PFxDu8VCQImXHyG74Fo=' 'strict-dynamic'; style-src 'self'; connect-src 'self'; base-uri 'none'">

<script integrity="sha256-1MV04PDgio8yygougSv5TFU7PFxDu8VCQImXHyG74Fo=" src="./script.js"></script>
```

### Warnings
```
[-] eval() Function in http://localhost:8080/9_eval/script.js (Line 1)
```

## Time
### System(sec)
```
0.033
0.033
0.03
0.027
0.025
0.031
0.023
0.027
0.03
0.027
```

### Browser(sec)
|before|after|
|:-:|:-:|
|||


# 10_Function_constructor
## Configured CSP
### CSP meta tag and script tag with integrity
```
<meta http-equiv="Content-Security-Policy" content="default-src *; script-src 'self' http://localhost:8080 'sha256-Ea7I3R+VZagjvvJqYc6qtkSUKGKA0ntjQ1WFYY1g+aM=' 'strict-dynamic'; style-src 'self'; connect-src 'self'; base-uri 'none'">

<script integrity="sha256-Ea7I3R+VZagjvvJqYc6qtkSUKGKA0ntjQ1WFYY1g+aM=" src="./script.js"></script>

```

### Warnings
```
[-] Function() Constructor in http://localhost:8080/10_Function_constructor/script.js (Line 1)
```

## Time
### System(sec)
```
0.031
0.024
0.027
0.025
0.031
0.032
0.024
0.023
0.031
0.043
```

### Browser(sec)
|before|after|
|:-:|:-:|
|||


# 11_all
## Configured CSP
### CSP meta tag and script tag with integrity
```
<meta http-equiv="Content-Security-Policy" content="default-src *; script-src 'self' http://localhost:8080 'sha256-gZmBnd4RznX/R53Rxj7t8Swp7HDysCKvy25yYD5QGfE=' 'sha256-b0wIol3V1kTL/TiBO5xkMC3MCsxQSGY/u6kUedKpvh4=' 'sha256-rr+HAv/rvjCyw6HOiKuNCRhCMB7YDTSkVk9fiq2+U2k=' 'sha256-llIEnPoqBHAkMW9ma2Fyh9gMKWEcYXva3SbAAxHpyYs=' 'sha256-1NYcwZPUGTVgwxOoV8wIyICVCMhB3F9b3H22XnvuEVw=' 'sha256-1MV04PDgio8yygougSv5TFU7PFxDu8VCQImXHyG74Fo=' 'sha256-J0lqB2JO0WBQyPz9aU9JR2mQidzgyYbA2hhrvHmSniE=' 'sha256-uxVHDkI2VVxiLrjNPK9Qlg7amPkHZVarv+HgmvH7IUI=' 'strict-dynamic'; style-src 'self' http://localhost:8080 'sha256-ElVvUDmzQMQ0Zpm2d4kqokClNu/iwMX7CtA5SFsBs3E='; connect-src 'self' https://code.jquery.com; base-uri 'none'">


<script integrity="sha256-gZmBnd4RznX/R53Rxj7t8Swp7HDysCKvy25yYD5QGfE=" src="./script.js"></script>
<script integrity="sha256-b0wIol3V1kTL/TiBO5xkMC3MCsxQSGY/u6kUedKpvh4=" src="./xhr_jquery.js"></script>
<script integrity="sha256-rr+HAv/rvjCyw6HOiKuNCRhCMB7YDTSkVk9fiq2+U2k=" src="./xhr_react.js"></script>
<script integrity="sha256-llIEnPoqBHAkMW9ma2Fyh9gMKWEcYXva3SbAAxHpyYs=" src="./inner_outer_html.js"></script>
<script integrity="sha256-1NYcwZPUGTVgwxOoV8wIyICVCMhB3F9b3H22XnvuEVw=" src="./document_write_writeln.js"></script>
<script integrity="sha256-1MV04PDgio8yygougSv5TFU7PFxDu8VCQImXHyG74Fo=" src="./eval.js"></script>
<script integrity="sha256-J0lqB2JO0WBQyPz9aU9JR2mQidzgyYbA2hhrvHmSniE=" src="./Function.js"></script>
```

### Warnings
```
[-] javascript: scheme in http://localhost:8080/11_all/index.php
[-] style attribute in http://localhost:8080/11_all/index.php
[-] innerHTML / outerHTML in http://localhost:8080/11_all/inner_outer_html.js (Line 5)
[-] innerHTML / outerHTML in http://localhost:8080/11_all/inner_outer_html.js (Line 6)
[-] document.write(ln) in http://localhost:8080/11_all/document_write_writeln.js (Line 1)
[-] document.write(ln) in http://localhost:8080/11_all/document_write_writeln.js (Line 2)
[-] eval() Function in http://localhost:8080/11_all/eval.js (Line 1)
[-] Function() Constructor in http://localhost:8080/11_all/Function.js (Line 1)
```

## Time
### System(sec)
```
0.067
0.066
0.068
0.078
0.089
0.068
0.07
0.069
0.076
0.073
0.072
0.075
0.067
0.082
0.072
0.068
0.071
0.087
0.08
0.078
0.095
0.075
0.066
0.072
0.073
0.068
0.068
0.07
0.074
0.063
```

### Browser(sec)
|before|after|
|:-:|:-:|
|||