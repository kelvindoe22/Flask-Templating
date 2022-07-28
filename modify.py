def change(word: str):
    if (href := word.find('href="')) != -1:
        start = href + 6
        end = word.find('"', start)

        if (param := word[start:end] ).startswith('assets') :
            final  = word[:start] + "{{ url_for('static', filename = '%s' ) }}" % param + word[end:]
            return final
        elif param.endswith('.html'):
            final = word[:start] + f'/{param[:-5]}' + word[end:]
            return final

    elif (src := word.find('src="')) != -1:
        start = src + 5
        end = word.find('"', start)
        if (param := word[start:end] ).startswith('assets') :
            final  = word[:start] + "{{ url_for('static', filename = '%s' ) }}" % param + word[end:]
            return final
    return word



