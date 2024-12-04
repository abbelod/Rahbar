// function saveItinerary() {
//     const clientInfo = {
//         name: document.getElementById('name').value,
//         phone: document.getElementById('phone').value,
//         startDate: document.getElementById('start-date').value,
//         endDate: document.getElementById('end-date').value,
//     };

//     const flightDetails = [];
//     const flightTable = document.getElementById('flight-table').getElementsByTagName('tbody')[0];
//     for (let i = 0; i < flightTable.rows.length; i++) {
//         const row = flightTable.rows[i];
//         flightDetails.push({
//             departureDate: row.cells[0].getElementsByTagName('input')[0].value,
//             arrivalDate: row.cells[1].getElementsByTagName('input')[0].value,
//             airline: row.cells[2].getElementsByTagName('input')[0].value,
//             arrivalTime: row.cells[3].getElementsByTagName('input')[0].value,
//             terminal: row.cells[4].getElementsByTagName('input')[0].value,
//         });
//     }

//     const itinerary = {
//         clientInfo: clientInfo,
//         flightDetails: flightDetails,
//     };

//     // Send data to backend using fetch
//     fetch('/planner/', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//         },
//         body: JSON.stringify(itinerary),
//     })
//     .then(response => response.json())
//     .then(data => {
//         if (data.status === 'success') {
//             alert('Itinerary saved successfully!');
//             document.getElementById("confirmation-message").innerText = "Itinerary saved successfully!";
//             document.getElementById("confirmation-message").style.display = "block";
//         } else {
//             alert('Failed to save itinerary');
//         }
//     })
//     .catch(error => {
//         console.error('Error:', error);
//         alert('Error saving itinerary');
//     });
// }

function saveItinerary() {
    const clientInfo = {
        name: document.getElementById('name').value,
        phone: document.getElementById('phone').value,
        startDate: document.getElementById('start-date').value,
        endDate: document.getElementById('end-date').value,
    };

    const flightDetails = [];
    const flightTable = document.getElementById('flight-table').getElementsByTagName('tbody')[0];
    for (let i = 0; i < flightTable.rows.length; i++) {
        const row = flightTable.rows[i];
        flightDetails.push({
            departureDate: row.cells[0].getElementsByTagName('input')[0].value,
            arrivalDate: row.cells[1].getElementsByTagName('input')[0].value,
            airline: row.cells[2].getElementsByTagName('input')[0].value,
            arrivalTime: row.cells[3].getElementsByTagName('input')[0].value,
            terminal: row.cells[4].getElementsByTagName('input')[0].value,
        });
    }

    const hotelDetails = [];
    const hotelTable = document.getElementById('hotel-table').getElementsByTagName('tbody')[0];
    for (let i = 0; i < hotelTable.rows.length; i++) {
        const row = hotelTable.rows[i];
        hotelDetails.push({
            checkInTime: row.cells[0].getElementsByTagName('input')[0].value,
            checkOutTime: row.cells[1].getElementsByTagName('input')[0].value,
            hotelName: row.cells[2].getElementsByTagName('input')[0].value,
            address: row.cells[3].getElementsByTagName('input')[0].value,
            inclusions: row.cells[4].getElementsByTagName('input')[0].value,
            roomDetails: row.cells[5].getElementsByTagName('input')[0].value,
        });
    }

    const activityDetails = [];
    const activityTable = document.getElementById('activity-table').getElementsByTagName('tbody')[0];
    for (let i = 0; i < activityTable.rows.length; i++) {
        const row = activityTable.rows[i];
        activityDetails.push({
            date: row.cells[0].getElementsByTagName('input')[0].value,
            destination: row.cells[1].getElementsByTagName('input')[0].value,
            activity: row.cells[2].getElementsByTagName('input')[0].value,
            remarks: row.cells[3].getElementsByTagName('input')[0].value,
        });
    }

    const itinerary = {
        clientInfo: clientInfo,
        flightDetails: flightDetails,
        hotelDetails: hotelDetails,
        activityDetails: activityDetails,
    };

    // Save to local storage
    localStorage.setItem('itinerary', JSON.stringify(itinerary));

    // Display confirmation message
    alert('Itinerary saved successfully!');
    
    // Optionally, display a confirmation div on the page instead of using alert
    document.getElementById("confirmation-message").innerText = "Itinerary saved successfully!";
    document.getElementById("confirmation-message").style.display = "block";
}
