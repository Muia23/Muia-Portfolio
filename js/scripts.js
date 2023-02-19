document.getElementById('prototypes').addEventListener('click', () => {
  console.log("Prototype");
  if (document.getElementById('proje').style.display == 'block'){
      document.getElementById('proje').style.display = 'none';
      document.getElementById('proto').style.display = 'flex';
      !document.getElementById('prototypes').classList.contains('active')? document.getElementById('prototypes').classList.add('active'): document.getElementById('prototypes').classList.remove('active');        
      !document.getElementById('projects').classList.contains('active')? document.getElementById('projects').classList.add('active'): document.getElementById('projects').classList.remove('active');        
  }
});

document.getElementById('projects').addEventListener('click', () => {
  console.log("Projects");
  let proj_tog = document.getElementById('projects');
  if (document.getElementById('proto').style.display == 'flex'){
      document.getElementById('proto').style.display = 'none';
      document.getElementById('proje').style.display = 'block';
      !document.getElementById('projects').classList.contains('active')? document.getElementById('projects').classList.add('active'): document.getElementById('projects').classList.remove('active');        
      !document.getElementById('prototypes').classList.contains('active')? document.getElementById('prototypes').classList.add('active'): document.getElementById('prototypes').classList.remove('active');
  }
});