function saveItinerary() {
    const clientInfo = {
        name: document.getElementById('name').value,
        phone: document.getElementById('phone').value,
        startDate: document.getElementById('start-date').value,
        endDate: document.getElementById('end-date').value,
    };

    const flightDetails = [];
    const flightTable = document.getElementById('flight-table').getElementsByTagName('tbody')[0];
    for (const row of flightTable.rows) {
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
    for (const row of hotelTable.rows) {
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
    for (const row of activityTable.rows) {
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
