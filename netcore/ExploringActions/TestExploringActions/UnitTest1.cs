using Xunit;
using ExploringActions.Controllers;
using System.Linq;

namespace TestExploringActions
{
    public class WeatherForecastControllerTests
    {
        [Fact]
        public void Get_ShouldReturn5Items()
        {
            // Arrange
            var controller = new WeatherForecastController();

            // Act
            var result = controller.Get();

            // Assert
            Assert.Equal(5, result.Count());
        }
    }
}
