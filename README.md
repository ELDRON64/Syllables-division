# Syllables-division

## description

this is a program that can divide a sentence in syllables

for now the languages supported are:

- Italian (ita)
- English (eng)
- Japanese (jpn)
- one (returns the letters)

more languages will be added in the future

## usage

```py
import syllables as sb
```

set the sentence and the default language by inizalizating an object:

```py
obj = sb.syllables("sentence","lang")
```

if you want to know the available languages use:

```py
lang = sb.langs()
print(lang)
```

to withdraw the sentence you can call:

```py
syllablesLang = obj.<lang>()
```

remove lang and use you language

or you can use:

```py
syllablesLang = obj.S
```

the S attribute will change if you call a obj.lang() function and switch to that language

you can also use:

```py
sentence = obj.F
```

to withdraw the original sentence
