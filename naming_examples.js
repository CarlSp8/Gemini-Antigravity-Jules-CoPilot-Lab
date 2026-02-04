/**
 * JavaScript Examples of Improving Variable and Function Names
 * This file demonstrates how to transform poorly named variables and functions
 * into clear, descriptive names that improve code readability.
 */

// ==========================================
// Example 1: Single Letter Variables
// ==========================================

// ❌ BAD: Single letter variables
function calc(a, b, c) {
    const t = a * b;
    const r = t * (1 + c);
    return r;
}

// ✅ GOOD: Descriptive variable names
function calculateTotalPriceWithTax(price, quantity, taxRate) {
    const subtotal = price * quantity;
    const totalWithTax = subtotal * (1 + taxRate);
    return totalWithTax;
}


// ==========================================
// Example 2: Array Methods
// ==========================================

// ❌ BAD: Vague arrow function parameters
const filterData = (arr) => arr.filter(x => x > 10);

// ✅ GOOD: Clear parameter names
const filterNumbersGreaterThanTen = (numbers) => 
    numbers.filter(number => number > 10);


// ==========================================
// Example 3: Object Properties
// ==========================================

// ❌ BAD: Unclear abbreviations
const usr = {
    id: 1,
    nm: "John",
    em: "john@example.com",
    dob: "1990-01-01"
};

// ✅ GOOD: Full, descriptive property names
const userProfile = {
    userId: 1,
    fullName: "John",
    emailAddress: "john@example.com",
    dateOfBirth: "1990-01-01"
};


// ==========================================
// Example 4: Event Handlers
// ==========================================

// ❌ BAD: Generic handler names
function handle(e) {
    e.preventDefault();
    // Do something
}

// ✅ GOOD: Descriptive handler names
function handleFormSubmission(event) {
    event.preventDefault();
    // Submit form data
}

function handleUserLoginClick(event) {
    event.preventDefault();
    // Process login
}


// ==========================================
// Example 5: Async Functions
// ==========================================

// ❌ BAD: Unclear async function purpose
async function get(id) {
    const response = await fetch(`/api/${id}`);
    return response.json();
}

// ✅ GOOD: Clear async function purpose
async function fetchUserDataById(userId) {
    const response = await fetch(`/api/users/${userId}`);
    return response.json();
}


// ==========================================
// Example 6: Boolean Variables
// ==========================================

// ❌ BAD: Unclear boolean names
function checkAuth(user) {
    const flag = user.loggedIn;
    const status = user.verified;
    return flag && status;
}

// ✅ GOOD: Clear boolean names with is/has/can prefix
function canUserAccessProtectedContent(user) {
    const isLoggedIn = user.loggedIn;
    const isVerified = user.verified;
    return isLoggedIn && isVerified;
}


// ==========================================
// Example 7: Constants
// ==========================================

// ❌ BAD: Unclear constant purpose
const MAX = 5;
const LIMIT = 100;
const TIME = 3000;

// ✅ GOOD: Clear constant purpose
const MAX_RETRY_ATTEMPTS = 5;
const API_REQUEST_LIMIT = 100;
const NOTIFICATION_TIMEOUT_MS = 3000;


// ==========================================
// Example 8: Class Names
// ==========================================

// ❌ BAD: Vague class names
class Manager {
    constructor(data) {
        this.data = data;
    }
    
    do() {
        return this.data.map(x => x * 2);
    }
}

// ✅ GOOD: Descriptive class and method names
class ShoppingCartManager {
    constructor(cartItems) {
        this.cartItems = cartItems;
    }
    
    calculateItemsWithDoubledQuantity() {
        return this.cartItems.map(item => item * 2);
    }
}


// ==========================================
// Example 9: Promise Chains
// ==========================================

// ❌ BAD: Generic variable names in promise chains
function badPromiseChainExample() {
    // In a real app: 
    // fetch('/api/data')
    //     .then(res => res.json())
    //     .then(d => {
    //         const r = d.filter(x => x.active);
    //         return r;
    //     });
}

// ✅ GOOD: Descriptive names in promise chains
function goodPromiseChainExample() {
    // In a real app:
    // fetch('/api/users')
    //     .then(response => response.json())
    //     .then(allUsers => {
    //         const activeUsers = allUsers.filter(user => user.active);
    //         return activeUsers;
    //     });
}


// ==========================================
// Example 10: Destructuring
// ==========================================

// ❌ BAD: Destructuring with unclear names
function process({ a, b, c }) {
    return a + b + c;
}

// ✅ GOOD: Destructuring with clear names
function calculateOrderTotal({ basePrice, shippingCost, taxAmount }) {
    return basePrice + shippingCost + taxAmount;
}


// ==========================================
// Example 11: Callback Functions
// ==========================================

// ❌ BAD: Generic callback names
function doSomething(data, cb) {
    const result = data.map(x => x * 2);
    cb(result);
}

// ✅ GOOD: Descriptive callback parameter names
function processUserData(users, onProcessingComplete) {
    const processedUsers = users.map(user => user * 2);
    onProcessingComplete(processedUsers);
}


// ==========================================
// Example 12: Reducer Functions
// ==========================================

// ❌ BAD: Generic reducer names
function badReducerExample(items) {
    const result = items.reduce((acc, curr) => {
        return acc + curr.val;
    }, 0);
    return result;
}

// ✅ GOOD: Clear reducer variable names
function calculateTotalPriceFromItems(orderItems) {
    const totalPrice = orderItems.reduce((runningTotal, currentItem) => {
        return runningTotal + currentItem.price;
    }, 0);
    return totalPrice;
}


// ==========================================
// Example 13: State Management
// ==========================================

// ❌ BAD: Unclear state variable names
function badStateExample() {
    let state = false;
    let data = null;
    let flag = true;
    return { state, data, flag };
}

// ✅ GOOD: Descriptive state variable names
function goodStateExample() {
    let isUserAuthenticated = false;
    let loadedUserProfile = null;
    let shouldShowNotification = true;
    return { isUserAuthenticated, loadedUserProfile, shouldShowNotification };
}


// ==========================================
// Example 14: Time and Intervals
// ==========================================

// ❌ BAD: Unclear timing variables
function badTimingExample() {
    const t = 5000;
    // Would call: setTimeout(() => {}, t);
}

// ✅ GOOD: Clear timing with units
function goodTimingExample() {
    const AUTO_SAVE_INTERVAL_MS = 5000;
    function saveUserProgress() {
        // Save user data
    }
    // Would call: setTimeout(() => { saveUserProgress(); }, AUTO_SAVE_INTERVAL_MS);
}


// ==========================================
// Example 15: DOM Manipulation
// ==========================================

// ❌ BAD: Generic element names
function badDOMExample() {
    if (typeof document !== 'undefined') {
        const el = document.querySelector('.item');
        const btn = document.getElementById('btn');
    }
}

// ✅ GOOD: Descriptive element names
function goodDOMExample() {
    if (typeof document !== 'undefined') {
        const productCardElement = document.querySelector('.product-card');
        const submitOrderButton = document.getElementById('submit-order-btn');
    }
}


// Test the examples
if (typeof window === 'undefined') {
    // Node.js environment - run tests
    console.log('✨ JavaScript Variable and Function Naming Examples');
    console.log('='.repeat(50));
    
    // Test Example 1
    console.log('\nExample 1: Calculate Price with Tax');
    const total = calculateTotalPriceWithTax(100, 2, 0.08);
    console.log(`Total: $${total.toFixed(2)}`);
    
    // Test Example 2
    console.log('\nExample 2: Filter Numbers > 10');
    const numbers = [5, 15, 8, 20, 12];
    const filtered = filterNumbersGreaterThanTen(numbers);
    console.log(`Filtered numbers: ${filtered}`);
    
    // Test Example 10
    console.log('\nExample 10: Calculate Order Total');
    const orderTotal = calculateOrderTotal({
        basePrice: 100,
        shippingCost: 15,
        taxAmount: 8.5
    });
    console.log(`Order total: $${orderTotal.toFixed(2)}`);
    
    console.log('\n' + '='.repeat(50));
    console.log('✅ All examples demonstrate improved naming!');
}
