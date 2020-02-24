
def process_csv(reader, writer):
    writer.write(f"Saw {len(reader.readlines())} lines" + "\n")
