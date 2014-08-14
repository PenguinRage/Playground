
public abstract class MyLinkedList implements LinkedList{

	private Node head;

	// The constructor method
	public MyLinkedList() {
		this.head = null;
	}

	// ------ Getters and Setters start --------

	public Node getHead() {
		return this.head;
	}
	// ------ Getters and Setters ends & Ze Germans are coming ------
	
	public boolean isEmpty() {
		if (this.head != null) {
			return false;
		}
		return true;
	}

	public int size() {
		int size = 0;
		Node current = head;
		while (current != null) {
			size += 1;
			current = current.getNext();
		}
		return size;
	}

	public Object get(int i) {
		int index = 0;
		Node current = head;
		while (current != null && index != i) {
			index += 1;
			current = current.getNext();
		}
		if (current == null)
			return null;
		return current.getElement();
	}
	
	public void add(Object o) {
		Node current = head;
        while (current.getNext() != null) {
            current = current.getNext();
        }
        current.setNext(new MyNode(o));
        if (head == null) {
            head = new MyNode(o);
            return;
        }
	}
	public void remove(Object o) {
		Node current = head;
        while (current.getNext() != null && current.getNext().getElement() != o) {
            current = current.getNext();
        }
        current.setNext(current.getNext().getNext());
        if (current.getNext() == null) {
            // Item not found
            return;
        }  
        if (head == null) {
            return;
        }
        if (head.getElement() == o) {
            head = head.getNext();
            return;
        }
	}

}
