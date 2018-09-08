/**
 * Write a description of interface Piece here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public interface Piece
{
    /***
     * How the piece move
     * Refer MovementType class
     */
    public MovementType movement();
    
    /***
     * PAWN can only move forward
     * while other piece can move in any direction
     */
    public boolean isOneDirection();
    
    /***
     * Can the piece upgrade
     * only PAWN can be upgrade
     */
    public boolean isUpgradable();
    
    /***
     * Get the piece type
     * Refer ChessType class
     */
    public ChessType getType();
}
