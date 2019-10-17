# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
def designerPdfViewer(h, word):
  max_h = 0
  for idx,height in enumerate(h):
    if (string.ascii_lowercase[idx] in word) and (height > max_h):
      max_h = height
  return max_h * len(word)
