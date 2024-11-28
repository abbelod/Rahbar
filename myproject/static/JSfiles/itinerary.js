function addFlightRow() {
    const table = document.getElementById('flight-table').getElementsByTagName('tbody')[0];
    const newRow = table.insertRow();

    newRow.innerHTML = `
        <td><input type="date" placeholder="Departure Date"></td>
        <td><input type="date" placeholder="Arrival Date"></td>
        <td><input type="text" placeholder="Airline"></td>
        <td><input type="time" placeholder="Arrival Time"></td>
        <td><input type="text" placeholder="Terminal"></td>
        <td><button onclick="removeRow(this)">Remove</button></td>
    `;
}

function addHotelRow() {
    const table = document.getElementById('hotel-table').getElementsByTagName('tbody')[0];
    const newRow = table.insertRow();

    newRow.innerHTML = `
        <td><input type="time" placeholder="Check-In Time"></td>
        <td><input type="time" placeholder="Check-Out Time"></td>
        <td><input type="text" placeholder="Hotel Name"></td>
        <td><input type="text" placeholder="Address"></td>
        <td><input type="text" placeholder="Inclusions"></td>
        <td><input type="text" placeholder="Room Details"></td>
        <td><button onclick="removeRow(this)">Remove</button></td>
    `;
}

function addActivityRow() {
    const table = document.getElementById('activity-table').getElementsByTagName('tbody')[0];
    const newRow = table.insertRow();

    newRow.innerHTML = `
        <td><input type="date" placeholder="Date"></td>
        <td><input type="text" placeholder="Destination"></td>
        <td><input type="text" placeholder="Activity"></td>
        <td><input type="text" placeholder="Remarks"></td>
        <td><button onclick="removeRow(this)">Remove</button></td>
    `;
}

function removeRow(button) {
    const row = button.parentNode.parentNode;
    row.parentNode.removeChild(row);
}

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
    alert('Itinerary saved successfully!');
}
