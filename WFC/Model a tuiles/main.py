import waveFunctionCollapse
import visual

grid = waveFunctionCollapse.initialize_grid(20)
grid[10][10].pre_collapse('SAND_TILE8')
grid = waveFunctionCollapse.run_wfc(grid)