from ipey.document.reader import Reader

r = Reader()
doc = r.read("ipes/groups.ipe")
doc.write("src/examples/output/groups_out.ipe")