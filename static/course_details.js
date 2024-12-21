function capitalizeLetter(str) {
    // Convert first letter to uppercase
    const capitalizedString = str.charAt(0).toUpperCase() + str.slice(1);

    return capitalizedString;
  }

  const topics = document.querySelectorAll('.topics-container span');
  for (let topic of topics) {
    const modifiedTopics = capitalizeLetter(topic.innerHTML);
    topic.innerHTML = modifiedTopics;
  }