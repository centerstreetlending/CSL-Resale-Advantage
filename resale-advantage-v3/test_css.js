const fs = require('fs');

let css = "";
for(let i=1; i<=6; i++) {
  let content = fs.readFileSync('webflow_embeds/0' + i + '_css.txt', 'utf8');
  // extract css
  let match = content.match(/<style>([\s\S]*?)<\/style>/);
  if(match) css += match[1] + "\n";
}

let braceCount = 0;
for(let i=0; i<css.length; i++) {
  if(css[i] === '{') braceCount++;
  if(css[i] === '}') braceCount--;
}
console.log("Final brace count:", braceCount);

let unclosed = false;
let stack = [];
for(let i=0; i<css.length; i++) {
  if(css.substring(i, i+2) === '/*') {
     let end = css.indexOf('*/', i+2);
     if(end === -1) {
       console.log("Unclosed comment at", i);
       unclosed = true;
       break;
     }
     i = end + 1;
  } else if(css[i] === '{') {
     stack.push(i);
  } else if(css[i] === '}') {
     if(stack.length === 0) {
       console.log("Unexpected } at", i);
       unclosed = true;
       break;
     }
     stack.pop();
  }
}
if(stack.length > 0) {
  console.log("Unclosed { at", stack);
} else if(!unclosed) {
  console.log("CSS syntax is structurally sound!");
}
