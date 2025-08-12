"""
./i18n.py
提供多语言支持
"""
import gettext
import os

class I18nManager:
    def __init__(self, default_lang='zh'):
        self.current_lang = default_lang
        self.translator = None
        self.setup_translation()
    
    def setup_translation(self):
        # 获取项目根目录
        base_path = os.path.dirname(os.path.abspath(__file__))
        locales_dir = os.path.join(base_path, 'locales')
        try:
            # 初始化gettext
            self.translator = gettext.translation(
                'messages', 
                localedir=locales_dir, 
                languages=[self.current_lang],
                fallback=True
            )
            self.translator.install()
        except:
            # 使用默认的空翻译
            self.translator = gettext.NullTranslations()
    
    def set_language(self, lang_code):
        self.current_lang = lang_code
        self.setup_translation()
    
    def get_supported_languages(self):
        return ['zh', 'en']
    
    def _(self, message):
        if self.translator:
            return self.translator.gettext(message)
        return message

i18n_manager = I18nManager()

def _(message):
    return i18n_manager._(message)

def set_language(lang_code):
    i18n_manager.set_language(lang_code)
