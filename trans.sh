curl --location 'http://0.0.0.0:5008/translate-file' \
     --form 'api_type="open_ai"' \
     --form 'translate_type="en_jp"'\
     --form file=@"$1"