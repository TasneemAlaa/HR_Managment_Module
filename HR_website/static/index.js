function addcheckout(recid) {
    fetch("/checkout", {
      method: "PUT",
      body: JSON.stringify({ recid: recid }),
    }).then((_res) => {
        
      window.location.href = "/";
    });
  }