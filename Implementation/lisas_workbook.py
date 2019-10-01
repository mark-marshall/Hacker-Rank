# https://www.hackerrank.com/challenges/lisa-workbook/problem

# Python
def workbook(n, k, arr):
  num_special_problems = 0
  cur_page = 0
  problem_on_page = 0;
  for chapter in arr:
    cur_page += 1
    problem_on_page = 0
    for i in range(chapter):
      problem = i + 1
      if problem_on_page + 1 > k:
        cur_page += 1
        problem_on_page = 1
      else:
        problem_on_page += 1
      if problem == cur_page:
        num_special_problems += 1
  return num_special_problems
  
# JavaScript
const workbook = (n,k,arr) => {
  let num_special_problems = 0
  let cur_page = 0
  let problems_on_page = 0
  arr.forEach(chapter => {
    cur_page += 1
    let problem_on_page = 0
    let i;
    for (i=0;i<chapter;i++){
      const problem = i + 1
      if(problem_on_page + 1 > k){
        cur_page += 1
        problem_on_page = 1;
      }
      else {
        problem_on_page += 1
      }
      if(problem === cur_page){
        num_special_problems += 1
      }
    }
  })
  return num_special_problems
}
