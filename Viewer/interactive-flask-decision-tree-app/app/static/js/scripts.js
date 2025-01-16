document.addEventListener('DOMContentLoaded', function() {
    const nodes = document.querySelectorAll('.node');

    nodes.forEach(node => {
        node.addEventListener('click', function() {
            const averagePrediction = this.getAttribute('data-average-prediction');
            alert('Средняя прогнозируемая величина в узле: ' + averagePrediction);
        });
    });
});