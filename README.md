# SM-Dictionaries

## Base dictionaries

These dictionaries are given as parameter to [Montreal Forced Aligner](https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner).

Four different languages are supported for the moment:
- French
- English
- German
- Spanish

## Consonant-vowel dicts

These dictionaries indicates for a given base dictionary which phones are consonants and which phonems are vowels.

This is used by [Sentence Mixing library](https://github.com/pop123123123/sentence-mixing)

## Add a new language

If you want to use a language that is supported by an [MFA pretrained model](https://montreal-forced-aligner.readthedocs.io/en/latest/pretrained_models.html) but not present in [SM-Dictionaries](https://github.com/nbusser/SM-Dictionaries), you can follow this procedure:
1. Find a text dictionary in the targetted language. This dictionary should be a big list of words
2. Use MFA's [g2p application](https://montreal-forced-aligner.readthedocs.io/en/latest/g2p_dictionary_generating.html):
    1. Download the corresponding [g2p pretrained model](https://montreal-forced-aligner.readthedocs.io/en/latest/pretrained_models.html#pretrained-g2p-models)
    2. Format you text dictionary by putting every word in lowercase, on the same line, separated by spaces
    3. Run command ```mfa g2p [g2p model] [dictionary] output.dict```
    4. Put every word in ```output.dict``` in uppercase
3. Create a consonant-vowel dict where you specify which phonemes are consonants and which phonemes are vowels. You should take example on the supported languages of this repository. Do not forget to add the line ```SPACE sp```

*Do noy hesitate to pull request your changes.*
