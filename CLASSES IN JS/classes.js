// Parent class with static method and instance properties
class Animal {
    constructor(name, type) {
        this.name = name;
        this.type = type;
    }

    // Static method that can be called without creating an instance
    static describe() {
        console.log("This is the Animal class.");
    }

    // Instance method to display properties
    displayProperties() {
        console.log(`Name: ${this.name}, Type: ${this.type}`);
    }
}

// Inherited class
class Dog extends Animal {
    constructor(name, breed) {
        super(name, "Dog");  // Call parent class constructor
        this.breed = breed;
    }

    // Method to display dog-specific property along with inherited properties
    displayDogProperties() {
        this.displayProperties();  // Call the parent class's method
        console.log(`Breed: ${this.breed}`);
    }
}

// Accessing the static method of the Animal class
Animal.describe(); // Static method, can be called without creating an instance

// Creating an instance of the Dog class (which inherits from Animal)
const myDog = new Dog("Buddy", "Golden Retriever");

// Accessing instance method to display properties of the Dog class
myDog.displayDogProperties(); // Access method from the Dog class
