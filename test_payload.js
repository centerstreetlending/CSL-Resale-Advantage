const { JSDOM } = require('jsdom');
const dom = new JSDOM(`
  <form id="form">
    <input name="first_name" value="John">
    <input name="last_name" value="Doe">
    <input name="email" value="john@example.com">
    <input name="phone" value="5551234567">
    <input name="property_address" value="">
    <input name="loan_number" value="">
    <select name="timeline">
      <option value="1-3mo" selected>In 1-3 months</option>
    </select>
    <input type="radio" name="intent" value="details" checked><span>Yes — send me details about the program</span>
    <input type="checkbox" name="consent" checked>
  </form>
`);
const document = dom.window.document;
const form = document.getElementById('form');

var timelineSelect = form.querySelector('select[name="timeline"]');
var timelineText = timelineSelect.options[timelineSelect.selectedIndex].text;
if (timelineSelect.value === "") timelineText = ""; 

var intentRadio = form.querySelector('input[name="intent"]:checked');
var intentText = intentRadio ? intentRadio.nextElementSibling.textContent : "";

var consentText = "I agree that Center Street Lending and its affiliates may contact me about the Investor Exit Advantage program by phone, email, or text at the information provided. Consent is not a condition of any loan. (Pending legal review.)";

var formData = new URLSearchParams();
formData.append("entry.1281752874", form.first_name.value);
formData.append("entry.511625773", form.last_name.value);
formData.append("entry.1714112113", form.email.value);
formData.append("entry.1515225399", form.phone.value);
formData.append("entry.964880898", form.property_address.value);
formData.append("entry.510331880", form.loan_number.value);
formData.append("entry.289374821", timelineText);
formData.append("entry.1894957803", intentText);
if (form.consent.checked) formData.append("entry.2092099687", consentText);

console.log(formData.toString());
