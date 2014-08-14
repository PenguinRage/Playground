public abstract class MyNode implements Node {
	private Object data;
	private Node next;

	// The constructor method
	public MyNode() {
		this.next = null;
	}

	// ---- Getters and Setters start ----------
	public Object getElement() {
		return this.data;
	}

	public Node getNext() {
		return this.next;
	}
	
	public void setElement(Object element) {
		this.data = element;
	}
	
	public void setNext(Node next) {
		this.next= next;
	}
	// ----- Getters and Setters end ---------

}
