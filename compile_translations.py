import os
from babel.messages.frontend import compile_catalog

def compile_translations():
    """使用 Babel 编译翻译文件"""
    locales_dir = os.path.join(os.path.dirname(__file__), 'locales')
    
    for lang in ['en', 'zh']:
        po_file = os.path.join(locales_dir, lang, 'LC_MESSAGES', 'messages.po')
        mo_file = os.path.join(locales_dir, lang, 'LC_MESSAGES', 'messages.mo')
        
        if os.path.exists(po_file):
            try:
                # 使用 Babel 编译
                from babel.messages.mofile import write_mo
                from babel.messages.pofile import read_po
                
                with open(po_file, 'r', encoding='utf-8') as f:
                    catalog = read_po(f)
                
                with open(mo_file, 'wb') as f:
                    write_mo(f, catalog)
                
                print(f"Compiled {lang} translations successfully")
            except Exception as e:
                print(f"Failed to compile {lang} translations: {e}")
    
    return True

if __name__ == "__main__":
    compile_translations()