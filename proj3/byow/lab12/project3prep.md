# Project 3 Prep

**For tessellating hexagons, one of the hardest parts is figuring out where to place each hexagon/how to easily place hexagons on screen in an algorithmic way.
After looking at your own implementation, consider the implementation provided near the end of the lab.
How did your implementation differ from the given one? What lessons can be learned from it?**

Answer:

一开始拆成多个图形去合成，后面发现旋转操作很难实现；后面发现按行等差打印，这种形式首先代码好写，其次以容易处理边界（如果要处理的话）

**Can you think of an analogy between the process of tessellating hexagons and randomly generating a world using rooms and hallways?
What is the hexagon and what is the tesselation on the Project 3 side?**

Answer:

对应房间，镶嵌结构可能代表连接房间与房间的走廊
**If you were to start working on world generation, what kind of method would you think of writing first? 
Think back to the lab and the process used to eventually get to tessellating hexagons.**

Answer:

先考虑单元的生成，再考虑单元的组成
**What distinguishes a hallway from a room? How are they similar?**

Answer:
走廊可以看作特殊的房间单位
