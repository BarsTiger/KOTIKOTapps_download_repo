import os
import subprocess, sys
try:
    import docx
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'python-docx'])
    import docx
import argparse

try:
    parser = argparse.ArgumentParser(description='Wordython - best interpreter for best IDE')
    parser.add_argument('script', nargs='?')

    args = parser.parse_args()
    script = args.script

    doc = docx.Document(script)
    script_name = str(script).split('.')[0] + '.py'

    code = ''

    with open(script_name, 'w') as f:
        for par in doc.paragraphs:
            code += str(par.text + '\n')
        f.write(code)

    os.system('python ' + script_name)

    os.remove(script_name)
except:
    raise
