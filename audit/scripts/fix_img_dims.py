from pathlib import Path

# Fix furniture-disassembly-and-reassembly-in-jeddah/index.html
p1 = Path('furniture-disassembly-and-reassembly-in-jeddah/index.html')
c1 = p1.read_text(encoding='utf-8')
target1 = '<img src="../assets/img/furniture-disassembly-and-reassembly-in-jeddah.webp"\n                            alt="فك وتركيب العفش بجدة"\n                            class="w-full max-w-2xl mx-auto h-auto rounded-2xl shadow-lg border border-gray-200 object-cover" loading="lazy" decoding="async">'
repl1 = '<img src="../assets/img/furniture-disassembly-and-reassembly-in-jeddah.webp"\n                            alt="فك وتركيب العفش بجدة"\n                            width="1086" height="1448" class="w-full max-w-2xl mx-auto h-auto rounded-2xl shadow-lg border border-gray-200 object-cover" loading="lazy" decoding="async">'
c1 = c1.replace(target1, repl1)
p1.write_text(c1, encoding='utf-8')

# Fix furniture-storage-in-jeddah/index.html
p2 = Path('furniture-storage-in-jeddah/index.html')
c2 = p2.read_text(encoding='utf-8')
target2 = '<img src="../assets/img/furniture-storage-in-jeddah.webp" alt="تخزين العفش بجدة في مستودعات مكيفة ومؤمنة"\n                        class="w-full max-w-3xl mx-auto h-auto rounded-2xl shadow-lg border border-gray-200 object-cover" loading="lazy" decoding="async">'
repl2 = '<img src="../assets/img/furniture-storage-in-jeddah.webp" alt="تخزين العفش بجدة في مستودعات مكيفة ومؤمنة"\n                        width="1024" height="1536" class="w-full max-w-3xl mx-auto h-auto rounded-2xl shadow-lg border border-gray-200 object-cover" loading="lazy" decoding="async">'
c2 = c2.replace(target2, repl2)
p2.write_text(c2, encoding='utf-8')

print("Image width and height successfully set.")
