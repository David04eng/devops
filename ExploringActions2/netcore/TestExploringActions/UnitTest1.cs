using Xunit;
using System.Linq;
using ExploringActions2.Controllers;

namespace TestExploringActions
{
    public class UnitTest1
    {
        [Fact]
        public void WeatherForecastController_Get_ReturnsForecasts()
        {
            // Arrange
            var controller = new WeatherForecastController();

            // Act
            var result = controller.Get();

            // Assert
            Assert.NotNull(result);           
            Assert.True(result.Any());        
        }
    }
}
