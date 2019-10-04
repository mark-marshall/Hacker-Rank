# https://www.hackerrank.com/challenges/taum-and-bday/problem

# Python
def taumBday(b, w, bc, wc, z):
  delta_col = None
  delta = None
  if abs(bc - wc) > z:
    if bc > wc:
      delta = bc - wc
      delta_col = 'white'
    elif wc > bc:
      delta = wc - bc
      delta_col = 'black'
  if delta:
    if delta_col == 'black':
      return (((b + w) * bc) + (z * w))
    elif delta_col == 'white':
      return (((w + b) * wc) + (z * b))
  elif not delta:
    return ((b * bc) + (w * wc))

# JavaScript
const taumBday = (b,w,bc,wc,z) => {
  let delta_col = null
  let delta = null
  if(Math.abs(bc - wc) > z){
    if(bc > wc){
      delta = bc - wc;
      delta_col = 'white';
    } else if (wc > bc){
      delta = wc - bc;
      delta_col = 'black';
    }
  }
  if(delta){
    if(delta_col === 'black'){
      return(((b + w) * bc) + (z * w))
    } else if (delta_col === 'white'){
      return(((w + b) * wc) + (z * b))
    }
  } else if (!delta){
    return((b * bc) + (w * wc))
  }
}
