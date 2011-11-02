from compress.filters.jspacker.jspacker import JavaScriptPacker
from compress.filter_base import FilterBase

class JSPackerFilter(FilterBase):
    def filter_js(self, js):
        p = JavaScriptPacker()
        result = p.pack(js, compaction=False, encoding=62, fastDecode=True)
        return result