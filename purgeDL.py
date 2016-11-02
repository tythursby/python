import os, time, shutil
def purgeDl(dir, age):
    print ("Scanning:", dir)
    for f in os.listdir(dir):
        now = time.time()
        filepath = os.path.join(dir, f)
        mod = os.stat(filepath).st_mtime
        if mod < now - age:
            if os.path.isfile(filepath):
                os.remove(filepath)
            elif os.path.isdir(filepath):
                shutil.rmtree(filepath)
                print ("Deleted: %s (%s)" % (f, mod))

purgeDl("/Users/Hal/Downloads", (7 * 86400))
