from ipey.document.reader import Reader

r = Reader()
doc = r.read("ipes/groups.ipe")
doc.write("examples/output/groups_out.ipe")