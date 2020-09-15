import ole

with ole.open('./blank.hwp') as f:
    print(f.list_streams())
    print('=' * 40)
    print(f.get_stream('FileHeader').read().decode('ascii'))