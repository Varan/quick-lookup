from typing import Callable, List, Tuple

from aqt import gui_hooks, mw
from aqt.qt import *

# Set up shortcut bindings from config.json
config = mw.addonManager.getConfig(__name__)
KANJI_SHORTCUT_KEY = QKeySequence(config['Kanji Lookup Shortcut'])
SENTENCE_SHORTCUT_KEY = QKeySequence(config['Sentence Lookup Shortcut'])

# We need two '%' symbols between each metacharacter
KANJI_LOOKUP_URL = config['URL for Kanji Lookup']
SENTENCE_LOOKUP_URL = config['URL for Sentence Lookup']
WORDS_LOOKUP_URL = config['URL for Word Lookup']


def on_shortcuts_change(state: str, shortcuts: List[Tuple[str, Callable]]) -> None:
    # Add reviewer shortcuts for looking up kanji details or sentences for the question of the card
    if state == "review":
        shortcuts.append((KANJI_SHORTCUT_KEY,
                          lambda: QDesktopServices.openUrl(QUrl(KANJI_LOOKUP_URL % filter_kana(mw.reviewer.card.q())))))
        shortcuts.append((SENTENCE_SHORTCUT_KEY,
                         lambda: QDesktopServices.openUrl(QUrl(SENTENCE_LOOKUP_URL % filter_kana(mw.reviewer.card.q())))))


gui_hooks.state_shortcuts_will_change.append(on_shortcuts_change)


def filter_kana(text):
    # Use unicode representation to filter out everything but kanji and kana (19968 through 40895 is kanji)
    kana = [x for x in text if 19968 <= ord(x) <= 40895 or 12353 <= ord(
        x) <= 12438 or 12449 <= ord(x) <= 12538 or ord(x) == 12293]
    return ''.join(kana)


def lookup_online(url, searchterm):
    # searches based on a url and a term
    if searchterm:
        QDesktopServices.openUrl(QUrl(url % searchterm))


def add_lookup_action(view, menu):
    # context menu, search for kanji info, word definitions, or example sentences
    selected = view.page().selectedText()
    if not selected:
        return

    selectedkana = filter_kana(selected)

    if selectedkana:
        suffixkana = (
            selectedkana[:10] + '..') if len(selectedkana) > 10 else selectedkana
        a = menu.addAction('Search "' + suffixkana + '" for kanji')
        a.triggered.connect(lambda: lookup_online(
            KANJI_LOOKUP_URL, selectedkana))

        b = menu.addAction('Search "' + suffixkana + '" for words')
        b.triggered.connect(lambda: lookup_online(
            WORDS_LOOKUP_URL, selectedkana))

        c = menu.addAction('Search "' + suffixkana + '" for sentences')
        c.triggered.connect(lambda: lookup_online(
            SENTENCE_LOOKUP_URL, selectedkana))


gui_hooks.webview_will_show_context_menu.append(add_lookup_action)
