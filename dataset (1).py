def get_custom_metadata(info, audio):

    prompt = info["relpath"]
    prompt = prompt.replace("_", " ")
    prompt = prompt.replace("/", " ")
    prompt = prompt.replace(".wav", "")


    return {"prompt": prompt}