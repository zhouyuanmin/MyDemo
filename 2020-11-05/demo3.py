import wordcloud
c = wordcloud.WordCloud()
txt = 'I have a good friend, and her name is Li Hua. We have become friends for about two years. She is very kind. When I step into the classroom for the first time, she helps me to get familiar with the strange environment. The most important thing is that we share the same interest, so we have a lot in common. '
c = c.generate(txt)
img = c.to_image()
img.show()

#
# print(f'c.width={c.width}')
# print(f'c.height={c.height}')
# print(f'c.min_font_size={c.min_font_size}')
# print(f'c.max_font_size={c.max_font_size}')
#
# print(f'{c.font_step}')
# print(f'{c.font_path}')
# print(f'{c.max_words}')
# print(f'{c.stopwords}')
# print(f'{c.mask}')
# print(f'{c.background_color}')