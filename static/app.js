document.getElementById("postData").addEventListener("click", postData);

function postData(event) {
  /*
    send array
    clear array
    clear list
    */

  console.log(actionArray);

  //   fetch("action", {
  //     method: "POST",
  //     headers: new Headers(),
  //     body: JSON.stringify({ commands: actionArray })
  //   })
  //     .then(res => res.json())
  //     .then(data => console.log(data))
  //     .catch(err => console.log(err));

  while (actionArray.length > 0) {
    actionArray.pop();
  }

  actionList.innerHTML = "";
  console.log(actionArray);
}

const actionArray = [];
const actionList = document.getElementById("action-list");

/*
Add all buttons to actions
event.target.dataset.action

*/

const buttons = document.getElementsByClassName("action-button");
const buttonsArray = [...buttons];
buttonsArray.forEach(button => {
  button.addEventListener("click", addAction);
});

const delayInput = document.getElementById("delay-input");

function addAction(event) {
  // Just add the string from the action?
  // How should the control work?
  const action = event.target.dataset.action;
  const delay = delayInput.value;
  const newListItem = `<li>${action} for ${delay > 0 ? delay : 1} second${
    delay > 1 ? "s" : ""
  }</li>`;

  actionList.innerHTML += newListItem;

  const actionObject = {
    action: action,
    delay: Number.isInteger(delay) ? delay : 1
  };
  actionArray.push(actionObject);

  // Need to add to an array, and a ul
}
