# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
def designerPdfViewer(h, word):
  max_h = 0
  chars = 'abcdefghijklmnopqrstuvwxyz'
  for idx,height in enumerate(h):
    if (chars[idx] in word) and (height > max_h):
      max_h = height
  return max_h * len(word)
  