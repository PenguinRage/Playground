package simulation;

import core.Direction;

/**
 * 
 * Simulation class
 * 
 * @author Ian Cleasby
 *
 */
public class Simulation {

	/**
	 * Initialise instance variables in this constructor
	 * 
	 * @param height - the height of the grid
	 * @param width - the width of the grid
	 * @param antStartI - the original I coordinate of the ant
	 * @param antStartJ - the original J coordinate of the ant
	 * @param originalDirection - the original direction the ant is facing
	 */
	int height;
	int width;
	int antStartI;
	int antStartJ;
	Direction originalDirection;
	int maxTimeSteps;
	Ant ant;
	Grid grid;

	public Simulation(int height, int width, int antStartI, int antStartJ,
			Direction originalDirection, int maxTimeSteps) {
		this.height=height;
		this.width=width;
		this.antStartI=antStartI;
		this.antStartJ=antStartJ;
		this.originalDirection=originalDirection;
		this.maxTimeSteps=maxTimeSteps;
		this.ant=new Ant(antStartI,antStartJ,originalDirection);
		this.grid=new Grid(height,width);
	}

	/**
	 * Execute a time step for the simulation.
	 * 
	 * The ant must:
	 * 		* move forward 1 space
	 * 			- if this movement cause it to move off the grid, 
	 * 				the simulation is completed.
	 * 		* rotate depending on the state of the cell the ant is occupying
	 * 			- if the cell is white, rotate left
	 * 			- otherwise, rotate right
	 * 		* change the state of the cell the ant is currently occupying
	 * 			- if the cell is white, it becomes black
	 * 			- otherwise, it becomes white
	 * 
	 * NOTE: Using the i,j coordinate system that are in the Ant class means that
	 *       0 <= i < height and 0 <= j < width
	 *
	 * NOTE: this method should do nothing if the simulation is completed.
	 */
	public void executeStep() {
		int i = ant.getIPos();
		int j = ant.getJPos();
		if (grid.isWhite(ant.getIPos(), ant.getJPos())){
			grid.setBlack(i, j);
			switch (ant.getDirection()) {
			case NORTH:
			{	ant.setDirection(Direction.EAST);
				ant.setJPos(++j);
				break;}
			case SOUTH:
			{	ant.setDirection(Direction.WEST);
				ant.setJPos(--j);
				break;}
			case EAST:
			{	ant.setDirection(Direction.SOUTH);
				ant.setIPos(++i);
				break;}
			case WEST:
			{	ant.setDirection(Direction.NORTH);
				ant.setIPos(--i);
				break;}
			}
		}

		else {
		grid.setWhite(i, j);
		switch (ant.getDirection()) {
		case NORTH:
		{	ant.setDirection(Direction.WEST);
			ant.setJPos(--j);
			break;}
		case SOUTH:
		{	ant.setDirection(Direction.EAST);
			ant.setJPos(++j);
			break;}
		case EAST:
		{	ant.setDirection(Direction.NORTH);
			ant.setIPos(--i);
			break;}
		case WEST:
		{	ant.setDirection(Direction.SOUTH);
			ant.setIPos(++i);
			break;}
		}
	}
}
	/**
	 * Method to check if the simulation is completed.
	 * 
	 * The simulation is completed if and only if:
	 * 		* it has reached the maximum time steps allowed
	 * 		* the ant has moved off the grid
	 * 
	 * @return true - the simulation is completed
	 * @return false - the simulation is not completed
	 */
	public boolean isCompleted() {
		if (ant.getIPos() >= maxTimeSteps || ant.getJPos() >=maxTimeSteps) {
		return true;
		}
		else { 
			return false;
		}
	}

	/**
	 * Method to return a copy of the current grid.
	 * 
	 * You should always return a copy of an object if you do not
	 * want your base object to be changed by any code calling this method.
	 * 
	 * @return a copy of the grid.
	 */
	public Grid getCopyOfGrid() {
		return grid;
	}

	/**
	 * Method to return a copy of the current ant.
	 * 
	 * You should always return a copy of an object if you do not
	 * want your base object to be changed by any code calling this method.
	 * 
	 * @return a copy of the ant.
	 */
	public Ant getCopyOfAnt() {
		return ant;
	}
}
