/// FOR CSS

///NAVIGATOR

const createBtn = document.querySelector('.create button');
const listBtn = document.querySelector('.list button');
const finishedBtn = document.querySelector('.finished button');
const createDiv = document.querySelector('.goals-create');
const listDiv = document.querySelector('.goals-list');
const finishedDiv = document.querySelector('.goals-finished');
const mainDiv = document.querySelector('.main');

const backBtn1 = document.querySelector('.back-btn1')
const backBtn2 = document.querySelector('.back-btn2')
const backBtn3 = document.querySelector('.back-btn3')

listDiv.style.display = "none";
finishedDiv.style.display = "none";
createDiv.style.display = "none";

createBtn.addEventListener('click', () => {
  mainDiv.style.display = 'none';
  createDiv.style.display = '';
});

listBtn.addEventListener('click', () => {
  mainDiv.style.display = 'none';
  listDiv.style.display = '';
});

finishedBtn.addEventListener('click', () => {
  mainDiv.style.display = 'none';
  finishedDiv.style.display = '';
});

backBtn1.addEventListener('click', () => {
  listDiv.style.display = "none";
  finishedDiv.style.display = "none";
  createDiv.style.display = "none";
  mainDiv.style.display = '';
});

backBtn2.addEventListener('click', () => {
  listDiv.style.display = "none";
  finishedDiv.style.display = "none";
  createDiv.style.display = "none";
  mainDiv.style.display = '';
});

backBtn3.addEventListener('click', () => {
  listDiv.style.display = "none";
  finishedDiv.style.display = "none";
  createDiv.style.display = "none";
  mainDiv.style.display = '';
});
