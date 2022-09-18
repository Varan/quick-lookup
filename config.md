### Customize shortcuts to your liking by changing them in the window to the left!

### If you are running macOS:

- `Ctrl` is `⌘` (command)
- `Alt` is `⌥` (option)
- `Meta` is `^` (control)

### You can also change the URLs that the add-on opens by doing the following:

1. Look up something (a sentence, words, or kanji) on your favorite website
   - e.g. looking up the [kanji details for 鉄塔 on jisho.org](https://jisho.org/search/鉄塔%20%23kanji)
2. Copy the link
   - e.g. copy https://jisho.org/search/鉄塔%20%23kanji
3. Replace the corresponding link in the configuration window to the left

   - Don't forget to make sure you haven't accidentally removed quotation marks or the comma that comes after (if there was one to begin with). They're important!
   - Replacing the link that comes after "URL for Kanji Lookup" with https://jisho.org/search/鉄塔%20%23kanji
     - Your computer may copy foreign characters (kana, kanji) with what looks like gibberish, but worry not! This is just sometimes how computers interpret foreign characters. We'll be replacing it in the next step!
       - e.g. `鉄塔` is represented as `%E9%89%84%E5%A1%94`.
       - This is called unicode for those of you interested! You can read about the representations of kana in [this article](https://memory.loc.gov/diglib/codetables/9.2.html) by the Library of Congress.
     - If this philosophically bothers you (as it did me), you can replace it in the configuration window with what you actually looked up.

4. Replace your query (the sentence, word, or kanji you looked up) with `%s`
   - Replace 鉄塔 with %s
   - e.g. https://jisho.org/search/%s%20%23kanji
     - This link won't actually do anything useful. `%s` just lets the add-on replace it with whatever you want to look up later!
5. You're done!

Finally, I'd like to thank you for using my add-on. I learned a lot by making it, and hope it helps you on your journey as much as it has, and continues to, help me!
